# me - this DAT.
# 
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
# 
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
# 
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.
import random
# 我们在这里定义一个全局列表，用于存储还未使用的数字
remaining_values = list(range(1,200))
# 定义全局变量跟踪当前段的起始索引
current_start_index = 1
current_end_index = current_start_index + 47  # 当前切片的结束索引
current_segment = [x for x in remaining_values if current_start_index <= x <= current_end_index]
def tableChange(dat):
    # 遍历convert DAT中的每一行和每一列
    for row in dat.rows():
        for cell in row:
            # 打印数值到textport
            print(cell.val)
    random_integer()

            
def onRowChange(dat, rows):
	return

def onColChange(dat, cols):
	return

def onCellChange(dat, cells, prev):
	return
def onSizeChange(dat):
	return
def random_integer():
    global remaining_values, current_start_index, current_end_index, current_segment

    # 如果当前切片为空，更新起始和结束索引，并创建新切片
    if not current_segment:
        current_start_index += 48
        current_end_index = current_start_index + 47
        current_segment = [x for x in remaining_values if current_start_index <= x <= current_end_index]
        
        # 如果所有值都用完了，重置全局列表和索引
        if not current_segment:
            remaining_values = list(range(1, 200))
            current_start_index = 1
            current_end_index = current_start_index + 47
            current_segment = [x for x in remaining_values if current_start_index <= x <= current_end_index]
    
    # 从当前切片中随机选择一个值，并从 remaining_values 和 current_segment 中删除它
    value = random.choice(current_segment)
    current_segment.remove(value)
    remaining_values.remove(value)
    
    # 计算在1-48范围内的映射值
    mapped_value = value - current_start_index + 1


    # 当列表为空时，重新填充它
   # if not remaining_values:
        #remaining_values = list(range(1, 49))
    
    # 从列表中随机选择一个数字，并删除它
    #value = random.choice(remaining_values)
    #remaining_values.remove(value)

    # 更新表格并打印值
    print("Mapped value before: ", mapped_value)  # 打印映射后的值
    op('randomValueTable')[0,0] = mapped_value
    print("Mapped value: ", mapped_value)  # 打印映射后的值
    print(op('randomValueTable'))  # 应当返回 DAT 的引用，而不是 None
    print(op('randomValueTable').numRows)  # 应当返回一个大于 0 的整数
    print(op('randomValueTable').numCols)  # 应当返回一个大于 0 的整数
   
    
    return value