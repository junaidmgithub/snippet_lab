
----------------Forign Table-------------------------

-- Ref: https://www.postgresql.org/message-id/c42ae6c78b5a0fc2ff05bb48ddca3733fc3212a4.camel%40cybertec.at

-- DROP FOREIGN DATA WRAPPER FTW_LOG;
-- DROP SERVER FTW_LOG_SERVER CASCADE;
-- DROP FOREIGN TABLE tbl_test_log;

CREATE EXTENSION postgres_fdw;

/* -- No need, "postgres_fdw" that is created by the extension is good enough.
CREATE FOREIGN DATA WRAPPER FTW_LOG
     HANDLER public.postgres_fdw_handler
     VALIDATOR public.postgres_fdw_validator;
*/

CREATE SERVER FTW_LOG_SERVER FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host 'localhost', dbname 'taas_log_03jan2023', port '5432');

CREATE USER MAPPING FOR postgres SERVER FTW_LOG_SERVER OPTIONS (user 'postgres', password 'admin');

CREATE FOREIGN TABLE tbl_test_log (
	pk_test_log_id BIGSERIAL,
	fk_test_id BIGINT NOT NULL,
	vhr_test_value VARCHAR(200) DEFAULT ''
) SERVER FTW_LOG_SERVER;

INSERT INTO public.tbl_test_log(
	pk_test_log_id, fk_test_id, vhr_test_value)
	VALUES (3, 1, 'hello3');
	
SELECT * FROM public.tbl_test_log;

UPDATE public.tbl_test_log SET vhr_test_value = 'NEW';
