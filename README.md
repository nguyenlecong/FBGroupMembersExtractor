# Facebook Group Members Extractor

<details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/nguyenlecong/FBGroupMembersExtractor/blob/main/requirements.txt) in a [**Python 3**](https://www.python.org/) environment.

```bash
git clone https://github.com/nguyenlecong/FBGroupMembersExtractor.git # clone
cd FBGroupMembersExtractor
pip install -r requirements.txt  # install
```
Download the correct version of [chromedriver](https://sites.google.com/chromium.org/driver/downloads?authuser=0) you are using and put it in the `asset` folder

</details>

<details open>
<summary>Extractor</summary>

1. Access Facebook Group **Member**
2. Set up [Collector](https://github.com/nguyenlecong/FBGroupMembersExtractor/blob/main/src/collector.js)[^1]
3. Set up [Scroller](https://github.com/nguyenlecong/FBGroupMembersExtractor/blob/main/src/scroller.js)[^2]
4. Download data
5. Configure Facebook Account and Extractor
6. Run Extractor: `python run.py`
7. The resulting file has the **same name** and is in the **same directory** with the file extension **xlsx**

</details>

[^1]: [Collector](https://github.com/floriandiud/facebook-group-members-scraper)
[^2]: [Scroller](https://github.com/Lucia361/Facebook-Groups-Extractor)