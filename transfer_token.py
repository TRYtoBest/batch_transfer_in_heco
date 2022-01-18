from web3 import Web3, HTTPProvider
from eth_account import Account
from pywebio.input import input,FLOAT,TEXT,radio
from pywebio.output import put_text,put_html
import os
import time
import usdt_abi
w3 = Web3(HTTPProvider("https://http-testnet.hecochain.com"))#heco测试网
usdt_contract = Web3.toChecksumAddress('0x04F535663110A392A6504839BEeD34E019FdB4E0')#usdt合约地址heco测试网
erc20token_contract =None
usdtcontract = w3.eth.contract(address=usdt_contract,abi=usdt_abi.usdtabi)
put_text('请在本文件当前目录下创建“private_key”文件，并填入私钥')
print('web3版本：%s'% w3.api)
print(w3.isConnected())
try:
  with open('.'+os.sep+'private_key','r') as private_k_file:
    private_key =private_k_file.read()
except Exception as e:
  put_text('未发现private_key文件'+str(e))
#print(private_key)
acc = Account.from_key(private_key=private_key)
fromAddress = Web3.toChecksumAddress(acc.address)
put_text('fromAddress:'+fromAddress)
#usdtcontract.functions.decimals().call()
try:
  put_text('主网币(HT)余额:'+str(Web3.fromWei(w3.eth.getBalance(acc.address),'ether')))
  put_text('usdt余额：'+str(usdtcontract.functions.balanceOf(fromAddress).call()/1000000))
except Exception as e:
  put_text('查询到余额'+str(e))

toAddress=input("转账目的地址：（如：0x4Af3Bb0C963a391854F0E09e05D571ee3CC44396）"
                "*多个地址用单个空格分开"
                "*或者每行一列的排序从记事本复制出来",type=TEXT)
transfer_type= radio('转账类型',options=['主网币(HT)','usdt（heco测试网）','其他代币请输入合约地址'])
toAddress_list=[addr.strip() for addr in toAddress.split(' ') if addr.strip()!='']
toAddress_confrim=str(toAddress_list)
trans_value=input("金额：（如：0.0001）\r*交易所充币有最低额度",type=FLOAT)
put_text('toAddress'+toAddress_confrim)
put_text('transfer_value:'+str(trans_value))
put_text('transfer_type:'+transfer_type)
confrim = input('请确认以上参数,输入ok',type=TEXT)
if confrim =='ok':
  no=1
  for toAddress in toAddress_list:
    if not toAddress:
      continue
    toAddress = Web3.toChecksumAddress(toAddress)
    nonce = w3.eth.getTransactionCount(fromAddress)
    gasPrice= w3.eth.gasPrice
    trans_value=float(trans_value) #以太坊数量
    value= Web3.toWei(trans_value,'ether')
    if transfer_type == '主网币(HT)':
      gas = w3.eth.estimateGas({'from':fromAddress,'to':toAddress,'value':value})
      trans_eth={
      'to': toAddress,
      'from': fromAddress,
      'value': value,
      'gasPrice':gasPrice,
      'gas':gas,
      'data':'',
      'nonce':nonce,
      'chainId':256 #对应链ID
      }
      txn_signed = w3.eth.account.signTransaction(trans_eth, private_key)  # 主网币
      txn_hash = w3.eth.sendRawTransaction(txn_signed.rawTransaction)
    if transfer_type == 'usdt（heco测试网）':
      trans_value_USDT = trans_value * 10**6
      gas=usdtcontract.functions.transfer(toAddress, int(trans_value_USDT)).estimateGas({'from':fromAddress})
      transaction_contract=usdtcontract.functions.transfer(toAddress, int(trans_value_USDT)).buildTransaction({'gasPrice':gasPrice,'gas':gas,'nonce':nonce})
      txn_signed_usdt = w3.eth.account.signTransaction(transaction_contract, private_key)#erc20代币
      txn_hash = w3.eth.sendRawTransaction(txn_signed_usdt.rawTransaction)
    if transfer_type == '其他代币请输入合约地址':
      if erc20token_contract==None:
        erc20token_contract = input("输入代币合约", type=TEXT)
      erc20token_contract = Web3.toChecksumAddress(erc20token_contract)
      erc20_contract_abi=w3.eth.contract(address=erc20token_contract,abi=usdt_abi.usdtabi)
      trans_value_erc20 = trans_value * 10**erc20_contract_abi.functions.decimals().call()
      gas=erc20_contract_abi.functions.transfer(toAddress, int(trans_value_erc20)).estimateGas({'from':fromAddress})
      transaction_contract_erc20=erc20_contract_abi.functions.transfer(toAddress, int(trans_value_erc20)).buildTransaction({'gasPrice':gasPrice,'gas':gas,'nonce':nonce})
      txn_signed_erc20 = w3.eth.account.signTransaction(transaction_contract_erc20, private_key)#erc20代币
      txn_hash = w3.eth.sendRawTransaction(txn_signed_erc20.rawTransaction)



    put_text('-----------------------------------当前第%s笔%s转账----------------------------------'% (no,transfer_type))
    no+=1
    put_text('转账hash：'+Web3.toHex(txn_hash))
    put_html('<a target="view_window" href=\"https://testnet.hecoinfo.com/tx/'+Web3.toHex(txn_hash)+'\">查看转账信息</a>')
    if transfer_type == '主网币':
      put_text(trans_eth)
      put_text('主网币(HT)转账金额：{:.10f} ht(小数点后保留10位)'.format(trans_value))
    elif transfer_type =='usdt（heco测试网）':
      put_text('usdt转账金额：'+str(trans_value)+'usdt')
    elif transfer_type == '其他代币请输入合约地址':
      put_text(erc20_contract_abi.functions.name().call()+'转账金额：' + str(trans_value) + erc20_contract_abi.functions.name().call())
    time.sleep(6.5)#避免nonce错误
  put_text('转账完毕！')
else:
  put_text('转账取消')
