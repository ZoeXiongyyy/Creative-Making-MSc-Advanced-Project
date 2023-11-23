# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
    # 获取Constant CHOP的引用
    constantCHOP = op('constant1')
    # 检查DAT to CHOP的值
    for i in range(1, 49):
        if val == i:
            # 设置相应的Constant CHOP值为1
            constantCHOP.par[f'value{i-1}'] = 1
        #else:
            # 将其它的值重置为0
           # constantCHOP.par[f'value{i-1}'] = 0
 	    # 检查是否所有值都为1
    all_values_one = all(constantCHOP.par[f'value{i-1}'] == 1 for i in range(1, 49))
    
    if all_values_one:
        # 如果所有值都为1，重置它们为0
        for i in range(1, 49):
            constantCHOP.par[f'value{i-1}'] = 0
    return