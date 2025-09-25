# Geometric & Harmonic mean
import math
nums = list(map(float, input("Enter numbers separated by space: ").split()))
geo_mean = math.prod(nums) ** (1/len(nums))
harmonic_mean = len(nums) / sum(1/x for x in nums)
print("Geometric Mean:", geo_mean)
print("Harmonic Mean:", harmonic_mean)