CREATE TABLE IF NOT EXISTS emails (
    e_id SERIAL NOT NULL PRIMARY KEY,
    user_id INT NOT NULL,
    email TEXT NOT NULL,

	CONSTRAINT fk_emails_user
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
);