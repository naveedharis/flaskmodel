import pandas as pd
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import scipy.sparse 
import requests
API_key = '89e8071cdf777af6e727e4cac6f685f9'

def get_recommendations(data,title, cosine_sim,indices):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:20]
    movie_indices = [i[0] for i in sim_scores]

    return data['id'].iloc[movie_indices]

def run_model(movie_id, movie_title):
    data = pd.read_csv('movie_model.csv', encoding='utf-8')
    movie_list = list()
    if movie_id not in data['id']:
        print("Id not in csv")
        recommendationresponse = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={API_key}&language=en-US&page=1').json()
        if 'results' in recommendationresponse.keys():
            for result in recommendationresponse['results']:
                movie_list.append(result['id'])
        return movie_list

    #count = CountVectorizer(stop_words='english')
    #count_matrix = count.fit_transform(data['soup'])
    count_matrix = scipy.sparse.load_npz('count_matrix.npz')
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

    data = data.reset_index()
    indices = pd.Series(data.index, index=data['title'])

    return list(get_recommendations(data,movie_title, cosine_sim2, indices))

#def main():
    #recommendations = run_model(98857,"Low Down")
    #print(recommendations)

#if __name__ == "__main__":
    #main()