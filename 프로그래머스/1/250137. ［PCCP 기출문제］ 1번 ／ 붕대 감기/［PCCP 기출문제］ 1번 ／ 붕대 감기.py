def solution(bandage, health, attacks):
    max_health = health
    last_attack_time = 0
    
    t, x, y = bandage # 시전 시간, 초당 회복량, 추가 회복량

    for attack_time, damage in attacks:
        # 1. 이전 공격과 현재 공격 사이의 자유 시간 계산
        gap = attack_time - last_attack_time - 1
        
        if gap > 0:
            # 자유 시간 동안의 총 회복량 = (초당 회복량 * 시간) + (보너스 회복 횟수 * 추가 회복량)
            recovery = (gap * x) + (gap // t * y)
            health = min(max_health, health + recovery)
        
        # 2. 공격 적용
        health -= damage
        
        # 3. 사망 판정
        if health <= 0:
            return -1
        
        # 4. 마지막 공격 시간 업데이트
        last_attack_time = attack_time
        
    return health