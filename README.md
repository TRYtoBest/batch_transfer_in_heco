######made with heart by TRYtoBest
<br/><br/>
##使用本脚本导致转账错误的资金损失概不负责
<br/>
##功能：<br/>
用于eth/heco/bsc等链的批量转账,一转多。每个地址用空格区分 或者直接从记事本复制(一行一收币地址)。<br/>

##如何运行于其他支持evm链
**本脚本仅用于heco测试网，如需要在其他主网上转账，请修改如下内容。**

第8行 `修改HTTPProvider`
```
w3 = Web3(HTTPProvider("https://http-testnet.hecochain.com"))#heco测试网
```
第9行 `修改合约地址`
```
usdt_contract = Web3.toChecksumAddress('0x04F535663110A392A6504839BEeD34E019FdB4E0')#usdt合约地址heco测试网
```
第62行 `修改为对应chainid，以太坊则直接删除即可`
```
'chainId':256 #对应链ID
```
第88行 `修改URL至目标链浏览器如：https://etherscan.io/tx/ `
```
put_html('<a target="view_window" href=\"https://testnet.hecoinfo.com/tx/'+Web3.toHex(txn_hash)+'\">查看转账信息</a>')
```
##然后按照如下方法使用

<br/>

##使用方法（heco测试网）
<br/>
python版本：3.7<br/>
需要 web3、eth_account、pywebio模块<br/>


```
使用pip3命令安装模块：

pip3 install -r requirements_transfer_token.txt

输入私钥：

在当前目录的private_key 中输入私钥，替换掉私钥

执行一下命令：

python3 transfer_token.py
```

在弹窗中输入相应信息<br/>
#按照提示进行操作
![transfer_token1.png](https://s2.loli.net/2022/01/18/EAxN6zCeRowS57p.png)
#多个地址如下图所示排列复制入对话框
![transfer_token1_1.png](https://s2.loli.net/2022/01/18/nCv48yFB2gLehzi.png)
#确认转账类型(有二次确认转账信息)
![transfer_token2.png](https://s2.loli.net/2022/01/18/DpYSBEV3hFHnIkl.png)
#转账效果
![transfer_token_check.png](https://s2.loli.net/2022/01/19/SbXsvHZkG3ny8UR.png)
