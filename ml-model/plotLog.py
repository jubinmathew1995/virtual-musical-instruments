import numpy as np
import matplotlib.pyplot as plt

h = np.load('log.npy')
# print(d)

# summarize history for accuracy
plt.plot(h.item().get('acc'))
plt.plot(h.item().get('val_acc'))
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(h.item().get('loss'))
plt.plot(h.item().get('val_loss'))
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

h.item().get('acc')