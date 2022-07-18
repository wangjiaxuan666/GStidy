# 对GWAS结果的sumstats文件质控

## 一般我们下载的sumstats文件是可能不对的

这个时候就需要我们进行一些手动的处理，结合ldsc软件的一些名称修改建议，再加上关于一些统计量的转变关系，最终形成了这个python包

- 支持自动识别列名，并进行补充
- 输入文件必须拥有几个必须的列名，`P`,`rsid`,以及`REF A1` 和`ALT A2`,否则怎么都转变不出来合格的格式

## 示例文件

简单做个用法说明和测试，首先已经有`[data/fake_table.GWAS.sumstats.tsv](../data/fake_table.GWAS.sumstats.tsv)`和数据库文件`[data/snp2chrpos.json](../data/snp2chrpos.json)`,`[data/snp2maf.json](../data/snp2maf.json)`。 当然这个三个文件，是我伪造的，
也是为了测试，所以搞得很小的测试文件。

### 先看看示例文件的结构

通过一下展示，可以发现json就是{key:values}这样的格式，而输入的矩阵，也是正常的GWAS sumstats 文件，只是少了很多应有的统计量和信息罢了。


```python
!head ../data/snp2chrpos.json
```

    {
    "rs62635278":"1:456",
    "rs2691333":"2:3455",
    "rs62635282":"3:4556657",
    "rs62635284":"5:4546",
    "rs77233895":"1:3435",
    "rs6682375":"2:1232",
    "rs6682385":"22:45546",
    "rs11580262":"8:232244",
    "rs3982632":"8:354546"



```python
!head ../data/fake_table.GWAS.sumstats.tsv
```

    rsid	A1	A2	N	P	OR
    rs62635278	C	A	4	0.7911	0.9818
    rs2691333	G	T	5	0.8735	0.9924
    rs62635282	G	C	4	0.802	0.9823
    rs62635284	A	G	4	0.7956	0.9806
    rs77233895	A	C	5	0.8814	0.9937
    rs6682375	A	G	4	0.8057	0.9817
    rs6682385	G	A	4	0.7992	0.9809
    rs11580262	A	G	4	0.7887	0.9784
    rs3982632	T	G	4	0.7992	0.9819


### 用GStidy进行处理

首先进入python的界面


```python
from gstidy import gstidy
data = gstidy("../data/fake_table.GWAS.sumstats.tsv")
data
```

    The input data lack of << SE >>, ===>:standard errors
    The input data lack of << Z >>, ===>:Z-score (0 --> no effect; above 0 --> A1 is trait/risk increasing)
    The input data lack of << BETA >>, ===>:[linear/logistic] regression coefficient (0 --> no effect; above 0 --> A1 is trait/risk increasing)
    The input data lack of << INFO >>, ===>:INFO score (imputation quality; higher --> better imputation)
    The input data lack of << FRQ >>, ===>:Allele frequency
    The input data lack of << PHENOTYPE >>, ===>:The disease PHENOTYPE, If you want add ,need -N parameter

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rsid</th>
      <th>A1</th>
      <th>A2</th>
      <th>N</th>
      <th>P</th>
      <th>OR</th>
      <th>SE</th>
      <th>BETA</th>
      <th>Z</th>
      <th>CHR</th>
      <th>BP</th>
      <th>MAF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>rs62635278</td>
      <td>C</td>
      <td>A</td>
      <td>4</td>
      <td>0.7911</td>
      <td>0.9818</td>
      <td>0.069343</td>
      <td>-0.018368</td>
      <td>-0.264882</td>
      <td>chr1</td>
      <td>456</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>rs2691333</td>
      <td>G</td>
      <td>T</td>
      <td>5</td>
      <td>0.8735</td>
      <td>0.9924</td>
      <td>0.047917</td>
      <td>-0.007629</td>
      <td>-0.159214</td>
      <td>chr2</td>
      <td>3455</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rs62635282</td>
      <td>G</td>
      <td>C</td>
      <td>4</td>
      <td>0.8020</td>
      <td>0.9823</td>
      <td>0.071218</td>
      <td>-0.017859</td>
      <td>-0.250760</td>
      <td>chr3</td>
      <td>4556657</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>rs62635284</td>
      <td>A</td>
      <td>G</td>
      <td>4</td>
      <td>0.7956</td>
      <td>0.9806</td>
      <td>0.075626</td>
      <td>-0.019591</td>
      <td>-0.259046</td>
      <td>chr5</td>
      <td>4546</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rs77233895</td>
      <td>A</td>
      <td>C</td>
      <td>5</td>
      <td>0.8814</td>
      <td>0.9937</td>
      <td>0.042360</td>
      <td>-0.006320</td>
      <td>-0.149195</td>
      <td>chr1</td>
      <td>3435</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rs6682375</td>
      <td>A</td>
      <td>G</td>
      <td>4</td>
      <td>0.8057</td>
      <td>0.9817</td>
      <td>0.075086</td>
      <td>-0.018470</td>
      <td>-0.245977</td>
      <td>chr2</td>
      <td>1232</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>rs6682385</td>
      <td>G</td>
      <td>A</td>
      <td>4</td>
      <td>0.7992</td>
      <td>0.9809</td>
      <td>0.075810</td>
      <td>-0.019285</td>
      <td>-0.254383</td>
      <td>chr22</td>
      <td>45546</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>rs11580262</td>
      <td>A</td>
      <td>G</td>
      <td>4</td>
      <td>0.7887</td>
      <td>0.9784</td>
      <td>0.081480</td>
      <td>-0.021837</td>
      <td>-0.267999</td>
      <td>chr8</td>
      <td>232244</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>rs3982632</td>
      <td>T</td>
      <td>G</td>
      <td>4</td>
      <td>0.7992</td>
      <td>0.9819</td>
      <td>0.071804</td>
      <td>-0.018266</td>
      <td>-0.254383</td>
      <td>chr8</td>
      <td>354546</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>
</div>



