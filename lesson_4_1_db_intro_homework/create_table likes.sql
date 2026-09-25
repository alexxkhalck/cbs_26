CREATE TABLE IF NOT EXISTS likes (
    like_id SERIAL NOT NULL PRIMARY KEY,
    user_id INT NOT NULL,
	post_id INT NOT NULL,

	CONSTRAINT fk_likes_user
		FOREIGN KEY (user_id)
		REFERENCES users(user_id),

	CONSTRAINT fk_likes_post
		FOREIGN KEY (post_id)
		REFERENCES posts(post_id)
);