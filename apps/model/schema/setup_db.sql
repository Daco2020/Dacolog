-- CREATE DATABASE dacolog CHARACTER SET UTF8;

-- mysql -u root -p

-- 데이터베이스 세팅 명령어
-- source /Users/daco/study/dacolog/apps/model/schema/setup_db.sql

use dacolog;

source /Users/daco/study/dacolog/apps/model/schema/categories.sql;
source /Users/daco/study/dacolog/apps/model/schema/logs.sql;
source /Users/daco/study/dacolog/apps/model/schema/tags.sql;
source /Users/daco/study/dacolog/apps/model/schema/log_tags.sql;