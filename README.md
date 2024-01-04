# pythoncrawler
Crawling index.hu website for article titles.
Prints results to standard output AND milan_horvath_index.txt

Solution:
1-find all 'h2' tags 
2-iterate through the list of h2 tags
3-find an 'a' tag inside the h2
4-if none is found then print text inside h2
5-if 'a' tag is found in h2 then print text inside the 'a' tag
