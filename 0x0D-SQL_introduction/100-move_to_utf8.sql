-- Converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- in my MySQL server.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SELECT CONVERT(binary CONVERT(name USING latin1) USING utf8mb4) FROM first_table;
