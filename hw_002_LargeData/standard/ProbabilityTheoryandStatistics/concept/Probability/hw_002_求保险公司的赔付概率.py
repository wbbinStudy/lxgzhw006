"""
保险公司
    5000张相同年龄,为期1年的保险单
        相互独立
        死亡率为0.0015 若一年内有人死亡赔付3万元
            求赔付总额不超过30万元的概率
                5000人 死亡率为0.0015
                =求死亡人数不超过10人的概率


"""
"""
参考答案

解:
    设这批投保人在一年内死亡人数为X,则
    X~(5000,0.0015)
    求死亡人数不超过30万/3万/人=10人
        P(X<=10)=∑_10_0(5000,k)(0.0015)**k*(1-0.0015)**(5000-k)
    若用泊松近似可以认为
        X~π(7.5),于是
        ...
        
ppois() R语言里面的泊松分布的求法
"""