import ast
import json
import datetime
import time
from poloniex import Poloniex
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.ticker_db

def insert_new_last(coinPair,currHour):

	db.tickPrice.insert({
		"timestamp_hour" : currHour,
		"tick" : coinPair,
		"last" : {
			"00" : 0,
			"01" : 0,
			"02" : 0,
			"03" : 0,
			"04" : 0,
			"05" : 0,
			"06" : 0,
			"07" : 0,
			"08" : 0,
			"09" : 0,
			"10" : 0,
			"11" : 0,
			"12" : 0,
			"13" : 0,
			"14" : 0,
			"15" : 0,
			"16" : 0,
			"17" : 0,
			"18" : 0,
			"19" : 0,
			"20" : 0,
			"21" : 0,
			"22" : 0,
			"23" : 0,
			"24" : 0,
			"25" : 0,
			"26" : 0,
			"27" : 0,
			"28" : 0,
			"29" : 0,
			"30" : 0,
			"31" : 0,
			"32" : 0,
			"33" : 0,
			"34" : 0,
			"35" : 0,
			"36" : 0,
			"37" : 0,
			"38" : 0,
			"39" : 0,
			"40" : 0,
			"41" : 0,
			"42" : 0,
			"43" : 0,
			"44" : 0,
			"45" : 0,
			"46" : 0,
			"47" : 0,
			"48" : 0,
			"49" : 0,
			"50" : 0,
			"51" : 0,
			"52" : 0,
			"53" : 0,
			"54" : 0,
			"55" : 0,
			"56" : 0,
			"57" : 0,
			"58" : 0,
			"59" : 0,
		},
		"low" : {
			"00" : 0,
			"01" : 0,
			"02" : 0,
			"03" : 0,
			"04" : 0,
			"05" : 0,
			"06" : 0,
			"07" : 0,
			"08" : 0,
			"09" : 0,
			"10" : 0,
			"11" : 0,
			"12" : 0,
			"13" : 0,
			"14" : 0,
			"15" : 0,
			"16" : 0,
			"17" : 0,
			"18" : 0,
			"19" : 0,
			"20" : 0,
			"21" : 0,
			"22" : 0,
			"23" : 0,
			"24" : 0,
			"25" : 0,
			"26" : 0,
			"27" : 0,
			"28" : 0,
			"29" : 0,
			"30" : 0,
			"31" : 0,
			"32" : 0,
			"33" : 0,
			"34" : 0,
			"35" : 0,
			"36" : 0,
			"37" : 0,
			"38" : 0,
			"39" : 0,
			"40" : 0,
			"41" : 0,
			"42" : 0,
			"43" : 0,
			"44" : 0,
			"45" : 0,
			"46" : 0,
			"47" : 0,
			"48" : 0,
			"49" : 0,
			"50" : 0,
			"51" : 0,
			"52" : 0,
			"53" : 0,
			"54" : 0,
			"55" : 0,
			"56" : 0,
			"57" : 0,
			"58" : 0,
			"59" : 0,
		},
		"high" : {
			"00" : 0,
			"01" : 0,
			"02" : 0,
			"03" : 0,
			"04" : 0,
			"05" : 0,
			"06" : 0,
			"07" : 0,
			"08" : 0,
			"09" : 0,
			"10" : 0,
			"11" : 0,
			"12" : 0,
			"13" : 0,
			"14" : 0,
			"15" : 0,
			"16" : 0,
			"17" : 0,
			"18" : 0,
			"19" : 0,
			"20" : 0,
			"21" : 0,
			"22" : 0,
			"23" : 0,
			"24" : 0,
			"25" : 0,
			"26" : 0,
			"27" : 0,
			"28" : 0,
			"29" : 0,
			"30" : 0,
			"31" : 0,
			"32" : 0,
			"33" : 0,
			"34" : 0,
			"35" : 0,
			"36" : 0,
			"37" : 0,
			"38" : 0,
			"39" : 0,
			"40" : 0,
			"41" : 0,
			"42" : 0,
			"43" : 0,
			"44" : 0,
			"45" : 0,
			"46" : 0,
			"47" : 0,
			"48" : 0,
			"49" : 0,
			"50" : 0,
			"51" : 0,
			"52" : 0,
			"53" : 0,
			"54" : 0,
			"55" : 0,
			"56" : 0,
			"57" : 0,
			"58" : 0,
			"59" : 0,
		}
	});

