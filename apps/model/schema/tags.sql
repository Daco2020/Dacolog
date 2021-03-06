CREATE TABLE tags(
    id         INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name       VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP on UPDATE CURRENT_TIMESTAMP
)CHARSET=utf8;