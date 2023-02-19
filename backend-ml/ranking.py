import openai

# constants
EMBEDDING_MODEL = "text-embedding-ada-002"

##sdfjsdlfksfklsd
openai.api_key = ""


from openai.embeddings_utils import (
    get_embedding,
    distances_from_embeddings,
    tsne_components_from_embeddings,
    chart_from_components,
    indices_of_nearest_neighbors_from_distances,
)


def get_embedding(text, model="text-embedding-ada-002"):
    """retrieve batch embeddings via api call"""
    #  text = text.replace("\n", " ")
    return openai.Embedding.create(input = text, model=model)['data']#[:]['embedding'] # returns [{'embedding}:[2,3], {..}, ..]

def embedding_from_string_list(
    string_list,
    model: str = EMBEDDING_MODEL
                                ) -> list:
    """Return embedding of given string in format [{'embedding}:[2,3], {..}, ..]"""
    print("string_list", string_list)
    embeddings_raw = get_embedding(string_list, model)

    #post processing [{'embedding}:[2,3], {..}, ..] into multi-d list
    embeddings_list = []
    for i in range(len(embeddings_raw)):
        embeddings_list.append(embeddings_raw[i]['embedding'])
    return embeddings_list

def retrieve_rankings_per_string( original_data_string_list,#: list[str], #data to be queried against
                                        index_of_source_string: int, # index to be queried
                                        k_nearest_neighbors: int = 2,
                                        model=EMBEDDING_MODEL,
                                    ): #-> list[int]:
    # get embeddings for all strings
    embeddings = embedding_from_string_list(original_data_string_list)
    # get the embedding of the source string
    query_embedding = embeddings[index_of_source_string]
    # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
    distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")
    # get indices of nearest neighbors (function from embeddings_utils.py)
    indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)

    # print out source string
    query_string = original_data_string_list[index_of_source_string]
    print(f"Source string: {query_string}")
    # print out its k nearest neighbors
    k_counter = 0
    for i in indices_of_nearest_neighbors:
        # skip any strings that are identical matches to the starting string
        if query_string == original_data_string_list[i]:
            continue
        # stop after printing out k articles
        if k_counter >= k_nearest_neighbors:
            break
        k_counter += 1

        # print out the similar strings and their distances
        print(
            f"""
        --- Recommendation #{k_counter} (nearest neighbor {k_counter} of {k_nearest_neighbors}) ---
        String: {original_data_string_list[i]}
        Distance: {distances[i]:0.3f}"""
        )

    return indices_of_nearest_neighbors

# #def retrieve_rankings_per_string( original_data_string_list,#: list[str], #data to be queried against
#                                     index_of_source_string_list, # index to be queried
#                                     k_nearest_neighbors: int = 2,
#                                     model=EMBEDDING_MODEL,
#                                     want_print: bool = True
#                                     ): #-> list[int]:
#     final_results = []

#     result_embeddings = embedding_from_string_list(original_data_string_list)
#     print("result_embeddings length: ", len(result_embeddings))
#     print("result_embeddings[0] type: ", type(result_embeddings[0]))

#     for idx in range(len(result_embeddings)):
#         # get embeddings for all strings
#         embeddings = result_embeddings[idx]
#         # get the embedding of the source string
#         query_embedding = embeddings[index_of_source_string_list[idx]]
#         # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
#         print("query_embedding", query_embedding, "embeddings", embeddings)
#         distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")
#         # get indices of nearest neighbors (function from embeddings_utils.py)
#         indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)


#         final_results.append(indices_of_nearest_neighbors) 

#         if want_print:
#             # print out source string
#             query_string = original_data_string_list[idx][index_of_source_string_list[idx]]
#             print(f"Source string: {query_string}")
#             # print out its k nearest neighbors
#             k_counter = 0
#             for i in indices_of_nearest_neighbors:
#                 # skip any strings that are identical matches to the starting string
#                 if query_string == original_data_string_list[idx][i]:
#                     continue
#                 # stop after printing out k articles
#                 if k_counter >= k_nearest_neighbors:
#                     break
#                 k_counter += 1

#                 # print out the similar strings and their distances
#                 print(
#                     f"""
#                 --- Recommendation #{k_counter} (nearest neighbor {k_counter} of {k_nearest_neighbors}) ---
#                 String: {original_data_string_list[idx][i]}
#                 Distance: {distances[i]:0.3f}"""
#                 )

#     return final_results


# #def retrieve_rankings_per_string2( original_data_string_list,#: list[str], #data to be queried against
#                                     index_of_source_string_list, # index to be queried
#                                     k_nearest_neighbors: int = 2,
#                                     model=EMBEDDING_MODEL,
#                                     want_print: bool = True
#                                     ): #-> list[int]:
#     final_results = []

#     result_embeddings = embedding_from_string_list(original_data_string_list)
#     print("result_embeddings length: ", len(result_embeddings))
#     print("result_embeddings[0] type: ", type(result_embeddings[0]))

#     for idx in range(len(result_embeddings)):
#         # get embeddings for all strings
#         embeddings = result_embeddings[idx]
#         # get the embedding of the source string
#         query_embedding = embeddings[index_of_source_string_list[idx]]
#         # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
#         print("query_embedding", query_embedding, "embeddings", embeddings)
#         distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")
#         # get indices of nearest neighbors (function from embeddings_utils.py)
#         indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)


#         final_results.append(indices_of_nearest_neighbors) 

#         if want_print:
#             # print out source string
#             query_string = original_data_string_list[idx][index_of_source_string_list[idx]]
#             print(f"Source string: {query_string}")
#             # print out its k nearest neighbors
#             k_counter = 0
#             for i in indices_of_nearest_neighbors:
#                 # skip any strings that are identical matches to the starting string
#                 if query_string == original_data_string_list[idx][i]:
#                     continue
#                 # stop after printing out k articles
#                 if k_counter >= k_nearest_neighbors:
#                     break
#                 k_counter += 1

#                 # print out the similar strings and their distances
#                 print(
#                     f"""
#                 --- Recommendation #{k_counter} (nearest neighbor {k_counter} of {k_nearest_neighbors}) ---
#                 String: {original_data_string_list[idx][i]}
#                 Distance: {distances[i]:0.3f}"""
#                 )

#     return final_results

# # def print_recommendations_from_strings( strings,#: list[str], #data to be queried against
# #                                         index_of_source_string: int, # index to be queried
# #                                         k_nearest_neighbors: int = 2,
# #                                         model=EMBEDDING_MODEL,
# #                                     ): #-> list[int]:
# #     # get embeddings for all strings
# #     embeddings = [embedding_from_string(string, model=model) for string in strings]
# #     # get the embedding of the source string
# #     query_embedding = embeddings[index_of_source_string]
# #     # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
# #     distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")
# #     # get indices of nearest neighbors (function from embeddings_utils.py)
# #     indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)

# #     # print out source string
# #     query_string = strings[index_of_source_string]
# #     print(f"Source string: {query_string}")
# #     # print out its k nearest neighbors
# #     k_counter = 0
# #     for i in indices_of_nearest_neighbors:
# #         # skip any strings that are identical matches to the starting string
# #         if query_string == strings[i]:
# #             continue
# #         # stop after printing out k articles
# #         if k_counter >= k_nearest_neighbors:
# #             break
# #         k_counter += 1

# #         # print out the similar strings and their distances
# #         print(
# #             f"""
# #         --- Recommendation #{k_counter} (nearest neighbor {k_counter} of {k_nearest_neighbors}) ---
# #         String: {strings[i]}
# #         Distance: {distances[i]:0.3f}"""
# #         )

# #     return indices_of_nearest_neighbors


features_existing_records_raw = "body, weight, bmi, height, medical history, hypertension, shortness of breath, covid"
features_transcript_extraction = "coughing"
inputs = features_existing_records_raw.split(", ")
print(inputs)

import numpy as np
indices = np.zeros(len(inputs), dtype=int).tolist()

retrieve_rankings_per_string(inputs, 1, k_nearest_neighbors=4)