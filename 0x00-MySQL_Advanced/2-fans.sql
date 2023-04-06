-- This script ranks country origins of bands, ordered by the number
-- of non-unique fans

SELECT origin, SUM(nb_fans) AS result_fans FROM metal_bands
GROUP BY origin
ORDER BY result_fans DESC;
