# # from progress.spinner import Spinner

# # spinner = Spinner("Spinner Processing", max=20)
# # for i in range(20):
# #     # Do some work
# #     spinner.next()
# # spinner.finish()

from progress.bar import Bar

bar = Bar("Bar Processing", max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()

