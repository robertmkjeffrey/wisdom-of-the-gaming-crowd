def report_features(feature_data, app_name, number):
    """Present the top n features."""
    adjective_count, positive_score, negative_score = feature_data
    
    # Convert the adjective count dictionary to a list of tuples, then sort by the count and get the top n.
    top_n_features = sorted(adjective_count.items(), key = lambda t: t[1], reverse=True)[:number]
    
    print(f"""Feature report for {app_name}:\n""")
    
    for feature in top_n_features:
        feature_name = feature[0]
        count = feature[1]
        pos = positive_score[feature_name]
        neg = negative_score[feature_name]
        percent_pos = 100 * pos / (pos + neg)
        print(f"""{feature_name} ({percent_pos:.2f}% positive) 
positive = {pos}, negative = {neg}, total = {count}""")
        print()