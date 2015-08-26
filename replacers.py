import re
import csv

replacement_patterns = [
     (r'won\'t', 'will not'),
     (r'can\'t', 'can not'),
     (r'i\'m', 'i am'),
     (r'ain\'t', 'is not'),
     (r'(\w+)\'ll', '\g<1> will'),
     (r'(\w+)n\'t', '\g<1> not'),
     (r'(\w+)\'ve', '\g<1> have'),
     (r'(\w+)\'s', '\g<1> is'),
     (r'(\w+)\'re', '\g<1> are'),
     (r'(\w+)\'d', '\g<1> would')
]

class RegexpReplacer(object):
      def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in
          patterns]

      def replace(self, text):
         s = text
         for (pattern, repl) in self.patterns:
             s = re.sub(pattern, repl, s)
         return s

#class CsvWordReplacer(WordReplacer):
#     def __init__(self, fname):
#       word_map = {}
#       for line in csv.reader(open(fname)):
#         word, syn = line
#         word_map[word] = syn
#       super(CsvWordReplacer, self).__init__(word_map)

