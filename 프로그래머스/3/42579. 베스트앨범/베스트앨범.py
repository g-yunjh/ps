from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_total = defaultdict(int) # 장르별 총 재생 횟수
    genre_songs = defaultdict(list) # 장르별 곡 정보 (재생수, 고유번호)
    
    for i in range(len(genres)):
        genre_total[genres[i]] += plays[i]
        genre_songs[genres[i]].append((plays[i], i))
        
    # 1. 많이 재생된 장르 순으로 정렬
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    for genre, total in sorted_genres:
        # 2. 장르 내에서 많이 재생된 순, 같으면 고유번호 낮은 순 정렬
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # 3. 장르별 최대 2곡까지 추가
        answer.extend([idx for play, idx in songs[:2]])
        
    return answer