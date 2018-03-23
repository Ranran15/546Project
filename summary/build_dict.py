# --
# --  Copyright (c) 2015, Facebook, Inc.
# --  All rights reserved.
# --
# --  This source code is licensed under the BSD-style license found in the
# --  LICENSE file in the root directory of this source tree. An additional grant
# --  of patent rights can be found in the PATENTS file in the same directory.
# --
# --  Author: Alexander M Rush <srush@seas.harvard.edu>
# --          Sumit Chopra <spchopra@fb.com>
# --          Jason Weston <jase@fb.com>

# -- Script to build the dictionary
import util 
import sys
import argparse
import pickle
# local utils = require('summary/util')

# cmd = torch.CmdLine()
# cmd:text()
# cmd:text()
# cmd:text('Build torch serialized version of a dictionary file.')
# cmd:text()
# cmd:text('Options')
# cmd:option('-inf', '', 'The input dictionary.')
# cmd:option('-outf', '', 'The output directory.')
# cmd:text()

sys.stdout.write("\n\n" )
sys.stdout.write('Build torch serialized version of a dictionary file.' )
sys.stdout.write("\n" )
sys.stdout.write('Options')
sys.stdout.write('-inf The input dictionary.')
sys.stdout.write('-outf The output directory.')
sys.stdout.write('\n')
sys.stdout.flush()



parser = argparse.ArgumentParser()
parser.add_argument("-inf", help="The input dictionary.")
parser.add_argument("-outf", help="The output directory")
args = parser.parse_args()
if args.inf:
    f = open(args.inf, 'r')
    word_id = 0
    local_dict = {'symbol_to_index':{}, 'index_to_symbol':{}}
    for l in f:
        word_id = word_id + 1
        word = util.string_split(l)[1]
        local_dict['symbol_to_index'][word] = word_id
        local_dict['index_to_symbol'][word_id] = word
if args.outf:
    with open(args.outf, 'wb') as handle:
        pickle.dump(local_dict, handle)

# opt = cmd:parse(arg)

# local f = io.open(opt.inf, 'r')
# local word_id = 0
# local dict = {symbol_to_index = {},
#               index_to_symbol = {}}
# for l in f:lines() do
#    word_id = word_id + 1
#    local word = utils.string_split(l)[1]
#    dict.symbol_to_index[word] = word_id
#    dict.index_to_symbol[word_id] = word
# end
# torch.save(opt.outf, dict)
