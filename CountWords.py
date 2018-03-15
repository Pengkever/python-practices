"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n most frequent words.
    arr = s.split(' ')
    arr.sort()
    index = 1
    word = arr[0]
    count = 1
    results = []
    while index < len(arr):
        if word == arr[index]:
            count += 1
        else:
            result = (word, count)
            results.append(result)
            word = arr[index]
            count = 1
        index += 1
    # the number of last word should be in the results
    results.append((word, count))
    results = sorted(results, key=lambda item:item[1], reverse=True)
    # return results
    top_n = results[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)
    # print count_words("a bb bb ccc ccc ccc dddd dddd dddd dddd", 2)


if __name__ == '__main__':
    test_run()
