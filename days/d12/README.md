# d12

Need to clean up this solution. Nice trick here is to calculate the border like it exists with whatever coordinates it could've had, even out of bounds, no need to draw anything out or put in arrays. GOTCHA on b is that you have to separate e.g. __(2, 5, "l")__ and __(2, 5, "r")__ since they are not the same side in the "real world".

- Probably there is a cleaner way to calculate the sides