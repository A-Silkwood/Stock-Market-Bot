CREATE OR REPLACE PROCEDURE insert_guild(id BIGINT)
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO guilds(id) VALUES ($1);
END;
$$;