#用于eth/heco/bsc等链的批量转账,一转多。每个地址用空格区分 或者直接从记事本复制(一行一收币地址)。
*本脚本仅用于heco测试网，如需要在其他主网上转账，请修改usdt合约地址及RPC。*

**使用本脚本导致转账错误的资金损失概不负责**

python版本：3.7
需要 web3、eth_account、pywebio模块


```
使用pip3命令安装模块：

pip3 install -r requirements_transfer_token.txt

输入私钥：

在当前目录的private_key 中输入私钥

执行一下命令：

python3 transfer_token.py
```

在弹窗中输入 相应信息
![transfer_token1](https://github.com/TRYtoBest/batch_transfer_in_heco/blob/main/transfer_token1.png)
![transfer_token2](https://github.com/TRYtoBest/batch_transfer_in_heco/blob/main/transfer_token2.png)
![transfer_token3](https://github.com/TRYtoBest/batch_transfer_in_heco/blob/main/transfer_token3.png)
![transfer_token4](https://github.com/TRYtoBest/batch_transfer_in_heco/blob/main/transfer_token4.png)