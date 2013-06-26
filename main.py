import datetime

from dbfpy import dbf

f=open('kladr.sql','w+')
f.write('''SET NAMES utf8;
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `altnames` (
  `oldcode` tinytext NOT NULL,
  `newcode` tinytext NOT NULL,
  `level` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `doma` (
  `name` tinytext NOT NULL,
  `korp` tinytext NOT NULL,
  `socr` tinytext NOT NULL,
  `code` tinytext NOT NULL,
  `index` tinytext NOT NULL,
  `gninmb` tinytext NOT NULL,
  `uno` tinytext NOT NULL,
  `ocatd` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `flat` (
  `name` tinytext NOT NULL,
  `code` tinytext NOT NULL,
  `index` tinytext NOT NULL,
  `gninmb` tinytext NOT NULL,
  `uno` tinytext NOT NULL,
  `np` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `kladr` (
  `name` tinytext NOT NULL,
  `socr` tinytext NOT NULL,
  `code` tinytext NOT NULL,
  `index` tinytext NOT NULL,
  `gninmb` tinytext NOT NULL,
  `uno` tinytext NOT NULL,
  `ocatd` tinytext NOT NULL,
  `status` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `socrbase` (
  `level` tinytext NOT NULL,
  `scname` tinytext NOT NULL,
  `socrname` tinytext NOT NULL,
  `kod_t_st` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `street` (
  `name` tinytext NOT NULL,
  `socr` tinytext NOT NULL,
  `code` tinytext NOT NULL,
  `index` tinytext NOT NULL,
  `gninmb` tinytext NOT NULL,
  `uno` tinytext NOT NULL,
  `ocatd` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
''')

for a in ['ALTNAMES','DOMA','FLAT','KLADR','SOCRBASE','STREET']:
    print a
    db = dbf.Dbf("./dbf/%s.dbf"%a)
    for rec in db:
        tmp=''
        for j in rec:
            tmp+="'%s',"%(j.decode('cp866').encode('utf-8'))
        f.write('''INSERT INTO `%s` VALUES (%s);\n''' % (a.lower(),tmp[:-1]))
f.close()
