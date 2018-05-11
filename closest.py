import random
import string


class Closest(object):
    def __init__(self):
        pass

    def generate_random_words(self):
        afile = open("random.txt", "w")

        try:
            for i in range(10000):
                line = ''
                for j in range(random.randint(1, 5)):
                    line += ''.join(random.choice(string.ascii_lowercase) for _ in range(8)) + ' '
                line += '\n'
                afile.write(line)
        except Exception as e:
            print str(e)

        afile.close()

    def levenshtein_distance(self, s, t):
        """
            iterative_levenshtein(s, t) -> ldist
            ldist is the Levenshtein distance between the strings
            s and t.
            For all i and j, dist[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        """
        rows = len(s) + 1
        cols = len(t) + 1
        dist = [[0 for x in range(cols)] for x in range(rows)]
        # source prefixes can be transformed into empty strings
        # by deletions:
        for i in range(1, rows):
            dist[i][0] = i
        # target prefixes can be created from an empty source string
        # by inserting the characters
        for i in range(1, cols):
            dist[0][i] = i

        for col in range(1, cols):
            for row in range(1, rows):
                if s[row - 1] == t[col - 1]:
                    cost = 0
                else:
                    cost = 1
                dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                     dist[row][col - 1] + 1,  # insertion
                                     dist[row - 1][col - 1] + cost)  # substitution

        return dist[row][col]

if __name__ == '__main__':
    closest_inst = Closest()
    closest_inst.generate_random_words()
