-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d5ebmck95iq2hk";

DROP TABLE IF EXISTS "location_comments";
DROP SEQUENCE IF EXISTS comments_id_seq;
CREATE SEQUENCE comments_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."location_comments" (
    "id" integer DEFAULT nextval('comments_id_seq') NOT NULL,
    "ref_id" integer NOT NULL,
    "comment" character varying NOT NULL,
    "username" character varying,
    CONSTRAINT "comments_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "user_login";
DROP SEQUENCE IF EXISTS user_login_id_seq;
CREATE SEQUENCE user_login_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."user_login" (
    "id" integer DEFAULT nextval('user_login_id_seq') NOT NULL,
    "username" character varying NOT NULL,
    "password" character varying NOT NULL,
    CONSTRAINT "user_login_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "user_login_username_key" UNIQUE ("username")
) WITH (oids = false);


DROP TABLE IF EXISTS "zip_data";
DROP SEQUENCE IF EXISTS zip_data_id_seq;
CREATE SEQUENCE zip_data_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."zip_data" (
    "id" integer DEFAULT nextval('zip_data_id_seq') NOT NULL,
    "zipcode" character varying NOT NULL,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "latitude" double precision NOT NULL,
    "longitude" double precision NOT NULL,
    "population" integer NOT NULL,
    "check_in" integer,
    CONSTRAINT "zip_data_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


-- 2018-07-12 13:30:59.255425+00
