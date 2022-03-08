def list_divider(count_subtask, list_obj):
	result = []
	subres = []
	for x, y in enumerate(list_obj):
		subres.append(y)
		if (x+1)%count_subtask == 0:
			result.append(subres)
			subres = []
	if len(subres) > 0:
		result.append(subres)

	return result