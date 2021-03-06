CREATE TABLE log_tags(
    id          INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    log_id      INT NOT NULL,
    tag_id      INT NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP on UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (log_id) REFERENCES logs (id),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
)CHARSET=utf8;