SELECT  -- 3
    o.ANIMAL_ID,           -- 유실된(입소 기록 없는) 입양 기록의 동물 ID
    o.NAME                 -- 이름 (NULL일 수도 있으나 문제에서 제외 조건 없음)
FROM ANIMAL_OUTS AS o      -- 1: 기준 테이블(입양 기록)
LEFT JOIN ANIMAL_INS  AS i -- 1: 입소 기록과 외래키(ANIMAL_ID)로 조인
    ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE i.ANIMAL_ID IS NULL  -- 2: 입소 기록이 없는(=유실된) 행만 남기기
ORDER BY o.ANIMAL_ID;      -- 4: ID 오름차순
