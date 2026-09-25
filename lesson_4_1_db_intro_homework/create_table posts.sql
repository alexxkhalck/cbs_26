CREATE TABLE IF NOT EXISTS posts (
    post_id SERIAL NOT NULL PRIMARY KEY,
    user_id INT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,

	CONSTRAINT fk_posts_user
		FOREIGN KEY (user_id)
		REFERENCES users(user_id)
);