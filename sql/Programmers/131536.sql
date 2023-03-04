-- 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요.
-- 결과는 회원 ID를 기준으로 오름차순 정렬해주시고, 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.


-- -------------------------------
-- My Answer
-- -------------------------------
SELECT DISTINCT xx.USER_ID, xx.PRODUCT_ID
FROM ONLINE_SALE as xx, ONLINE_SALE as yy
WHERE xx.ONLINE_SALE_ID != yy.ONLINE_SALE_ID 
    and xx.USER_ID = yy.USER_ID 
    and xx.PRODUCT_ID = yy.PRODUCT_ID
ORDER BY xx.USER_ID ASC, xx.PRODUCT_ID DESC


-- -------------------------------
-- Solution 1
-- -------------------------------
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC