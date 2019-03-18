beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


def ladderLength(beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        visited = set()
        visited.add(beginWord)

        if endWord not in wordList:
            return 0

        dist = 1

        queue = [beginWord]
        gg=[]
        gc=[]
        while queue:
            length = len(queue)
            for i in range(length):
                w = queue.pop(0)
                print('pop0 '+w )
                gg.append(w)
                gc.append(length)
                if w == endWord:
                    print(gg)
                    print(gc)
                    return dist
                for i in range(len(w)):
                    chars = list(w)

                    for j in range(ord('a'), ord('z') + 1):
                        chars[i] = chr(j)
                        tmp = ''.join(chars)
                        if tmp in wordList:
                            wordList.remove(tmp)
                            print(wordList)
                            queue.append(tmp)
                            print(queue)
            dist += 1
        print(gg)
        return 0

print(ladderLength(beginWord, endWord, wordList))