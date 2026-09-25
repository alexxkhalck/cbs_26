CREATE TABLE IF NOT EXISTS comments (
    comment_id SERIAL NOT NULL PRIMARY KEY,
    user_id INT NOT NULL,
	post_id INT NOT NULL,
    com TEXT NOT NULL,

	CONSTRAINT fk_comments_user
		FOREIGN KEY (user_id)
		REFERENCES users(user_id),

	CONSTRAINT fk_comments_post
		FOREIGN KEY (post_id)
		REFERENCES posts(post_id)
);