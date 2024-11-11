# 1. HBase project
## 2. Social media posts analysis with the help of Apache HBase
## 3. Roadmap

3.1. Accessing posts from [Twitter](x.com) via [Twitter API](https://developer.x.com/en/docs/x-api). The proper request for access to [Twitter API](https://developer.x.com/en/docs/x-api) has been filed: Request:
*"I'd like to use X APIs for my studies project related to big data analysis - I'd like to collect some arbitrary user posts and then using natural language processing try to determine the tone and emotion they convey. The use case is simply educational."*
- bearer token obtained
- post successfully read from the platform
- there are lots of shortcommings sadly:
    - cap of 100 read requests (posts) a month
    - 15 minutes cooldown between consecutive read requests

3.2 Designing HBase Schema for [Twitter](x.com) posts. 

3.3 Ingesting Data into HBase

3.4 Analyzing Data
