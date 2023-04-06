DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT SUM(score * weight) / SUM(weight) FROM users AS US
	JOIN corrrections as COR ON US.id=COR.user_id
	JOIN projects AS PRO ON COR.project_id=PRO.id WHERE US.id=user_id);

    UPDATE users SET weighted_score = avg_score WHERE id = user_id;
END//

DELIMITER ;
