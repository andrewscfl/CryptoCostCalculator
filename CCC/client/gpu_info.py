from subprocess import check_output

class gpu_info:
    def __init__(self):
        pass

    def get_gpu_power_draw(self):
        out = check_output(['nvidia-smi', '--query-gpu=power.draw','--format=csv'])
        out = str(out)
        format = out.replace("\\r","").replace('\\n','').replace('b\'power.draw [W]','').replace(' W\'','')
        return float(format)

    def get_gpu_utilization(self):
        out = check_output(['nvidia-smi', '--query-gpu=utilization.gpu','--format=csv'])
        out = str(out)
        format = out.replace("\\r","").replace('\\n','').replace("b\'utilization.gpu [%]","").replace(' %\'','')
        return float(format)

    def get_gpu_temperature(self):
        out = check_output(['nvidia-smi', '--query-gpu=temperature.gpu','--format=csv'])
        out = str(out)
        format = out.replace('b\'temperature.gpu','').replace("'","").replace("\\r","").replace('\\n','')
        return float(format)

    def get_gpu_name(self):
        out = check_output(['nvidia-smi', '--query-gpu=name','--format=csv'])
        out = str(out)
        format = out.replace('b\'name\\r\\n','').replace("\\r\\n\'",'')
        return format
        
gpu = gpu_info()

stats = {
    'power_draw' : gpu.get_gpu_power_draw(),
    'utilization' : gpu.get_gpu_utilization(),
    'temperature' : gpu.get_gpu_temperature(),
    'name' : gpu.get_gpu_name()
}

print(str(stats))


