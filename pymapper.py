import logging
import math
from bitstring import *

#Set logging library configuration
logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s', datefmt='%H:%M:%S')

#List of blocks to treat as invisible by default
ignore_defaults = ["minecraft:air",
                  "minecraft:cave_air",
                  "minecraft:void_air",
                  "minecraft:light_block",
                  "minecraft:barrier",
                  "minecraft:structure_void"]

def section_data(chunk_section):
    #Initialize logger
    logger = logging.getLogger('section_data')
    #Get block palette
    logger.debug("Retrieving block palette")
    try:
        block_palette = chunk_section["block_states"]["palette"]
    except:
        logger.warning("Block palette not found, ignoring chunk")
        return ["minecraft:air" for i in range(4096)]
    logger.debug("Palette items: " + str(len(block_palette)))
    #Get bit length
    bit_len = (len(block_palette) - 1).bit_length()
    #Get blocks per integer
    blocks_per_int = int(64/bit_len)
    #Get integer count
    int_count = math.ceil(4096/blocks_per_int)
    logger.debug("Bit length: " + str(bit_len))
    logger.debug("Blocks per integer: " + str(blocks_per_int))
    logger.debug("Integer count: " + str(int_count))
    #Load block data into memory
    logger.debug("Retrieving block placement data")
    block_data = dump_section(chunk_section)
    #Create bit array index
    logger.debug("Creating bit array index")
    block_index = [block_data[i:i+64] for i in range(0, len(block_data), 64)]
    logger.debug("Bit array index: " + str(len(block_index)) + " long integers")
    #Create integer list
    logger.debug("Creating integer list")
    integer_list = [a[b:b+bit_len].int for a in block_index for b in range(0, len(block_index), bit_len) if len(a[b:b+bit_len]) == bit_len]
    logger.debug("Integer list: " + str(len(integer_list)) + " items")

def get_topmost(chunk, ignore_list=ignore_defaults):
    section_count = ""

#Dumps block placement data into a bit array
def dump_section(section):
    raw_bytes = bytes()
    for integer in section["block_states"]["data"]:
        raw_bytes = raw_bytes + integer.to_bytes(8, 'little')
    return BitArray(raw_bytes)