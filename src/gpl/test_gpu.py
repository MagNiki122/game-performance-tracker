import subprocess

def monitor_gpu_fast():
    # 'typeperf' natively polls Windows counters. 
    # '-si 1' tells it to push updates exactly every 1 second.
    cmd = ['typeperf', r'\GPU Engine(*)\Utilization Percentage', '-si', '1']
    
    try:
        # Start the process in the background
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print("Tracking GPU Usage (Press Ctrl+C to stop)...")
        
        # Read the output line-by-line as Windows generates it in real-time
        for line in process.stdout:
            line = line.strip()
            
            # Skip empty lines, column headers, and system messages
            if not line or line.startswith('"(PDH-CSV') or line.startswith('The command'):
                continue
            
            # The output is comma-separated. The first item is the timestamp, the rest are GPU engines
            parts = line.split(',')
            if len(parts) > 1:
                total_usage = 0.0
                
                # Loop through all engine values and sum the active ones
                for val in parts[1:]:
                    cleaned_val = val.replace('"', '').strip()
                    if cleaned_val:
                        try:
                            num = float(cleaned_val)
                            if num > 0:
                                total_usage += num
                        except ValueError:
                            pass
                
                # Cap the maximum display at 100% 
                total_usage = min(100.0, total_usage)
                print(f"Current GPU Utilization: {total_usage:.2f}%")
                
    except KeyboardInterrupt:
        # Kill the background process cleanly when you press Ctrl+C
        process.terminate()
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor_gpu_fast()