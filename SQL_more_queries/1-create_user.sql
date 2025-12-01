-- Show grants for user_0d_1 if exists
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2 if exists
-- user_0d_2 hələ mövcud olmaya bilər, error çıxmasın deyə bu hissəni əvvəlcə yarada bilərsən
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
