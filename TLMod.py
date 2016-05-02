from smbus import SMBus
import math, csv, time 

bus = SMBus(1)

adc_address1 = 0x48   # Imposta indirizzo 000 ADC 

adc_channel1 = 0x40   # 
adc_channel2 = 0x41   # Imposta indirizzi canali
adc_channel3 = 0x42   # con risoluzione di 8 bit
adc_channel4 = 0x43   # 

R1 = 15000.0          # Resistenza R1 
R2 = 15000.0          # Resistenza R2
R_th0 = 10000.0       # Resistenza riferimento termistore a 25 c
R_fr0 = 70000.0       # Resistenza fotoresistore con illuminamento IL unitario 

V_IN = 3.3            # Tensione alimentazione partitori tensione
V_REF = 3.3           # Tensione riferimento misura ADC
A = 0.00335402        # Steinhart-Hart Costante A
B = 0.000256985       # Steinhart-Hart Costante B
C = 2.62013e-6        # Steinhart-Hart Costante C
D = 6.38309e-8        # Steinhart-Hart Costante D

pB = 4100.0           # Costante parametro B

K = 6.0               # Fattore dissipazione K 6mV C

Pend = 0.7            # Valore Gamma fotoresistenza
	
def Temperatura():
	bus.write_byte(adc_address1,adc_channel1)
	raw_val = bus.read_byte(adc_address1)
	raw_val = bus.read_byte(adc_address1)
	raw_val = bus.read_byte(adc_address1)
	
	hex_val = hex(raw_val)[2:].rstrip('L')
	dec_val = int(hex_val,16)
	
	V = (dec_val * V_REF) / 256.0
	R_th = (R1 * V) / (V_IN - V)

	logR = math.log(R_th / R_th0)
	logR2 = logR**2
	logR3 = logR**3
	Stein = 1.0 / (A + B * logR + C * logR2 + D * logR3)
	
	# Conversione in gradi Celsius e applicazione fattore di dispersione
	Celsius = round(Stein - 273.15 - V**2 / (K * R_th),2)
	
	print (Celsius)

def Lux():
	bus.write_byte(adc_address1,adc_channel2)
	raw_val2 = bus.read_byte(adc_address1)
	raw_val2 = bus.read_byte(adc_address1)
	raw_val2 = bus.read_byte(adc_address1)
	hex_val2 = hex(raw_val2)[2:].rstrip('L')
	dec_val2 = int(hex_val2,16)
	
	V2 = (dec_val2 * V_REF) / 256.0
	
	R_lm = (R1 * V2) / (V_IN - V2)
	
	# Calcolo della luminosita con 2 decimali
	Lux = round((R_lm / R_fr0)**(1.0/-Pend),2)
	
	print (Lux)