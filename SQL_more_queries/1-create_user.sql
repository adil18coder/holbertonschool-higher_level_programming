-- 1-create_user.sql
-- Yaradılırsa, mövcud istifadəçini silmədən istifadəçi əlavə edilir
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- user_0d_1-ə bütün privilegelər verilir
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Dəyişiklikləri təsdiqləyirik
FLUSH PRIVILEGES;
