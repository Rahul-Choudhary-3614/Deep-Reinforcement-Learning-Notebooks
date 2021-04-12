import tensorflow as tf
from tensorflow.python.framework import tensor_shape


class noisy_dense(tf.keras.Model):
  def __init__(self,units=32,activation_fn=None):
    super(noisy_dense,self).__init__()
    self.units = units
    self.activation_fn = activation_fn

  def f(self,x):
    return tf.multiply(tf.sign(x), tf.pow(tf.abs(x), 0.5))
  
  def build(self, input_shape):
    # Initializer of \mu and \sigma
    input_shape = tensor_shape.TensorShape(input_shape)
    last_dim = tensor_shape.dimension_value(input_shape[-1])

    self.w_mu = self.add_weight(
        shape=(last_dim, self.units),
        initializer="random_normal",
        trainable=True,
        )
    self.w_sigma = self.add_weight(
        shape=(last_dim, self.units), initializer="random_normal", trainable=True
        )
    
    self.b_mu = self.add_weight(
        shape=(self.units,),
        initializer="random_normal",
        trainable=True,
        )
    self.b_sigma = self.add_weight(
        shape=(self.units,), initializer="random_normal", trainable=True
        )

  def call(self,inputs):
    p = tf.random.normal((tf.shape(inputs)[1],1))
    q = tf.random.normal((1, self.units))
    f_p = self.f(p)
    f_q = self.f(q)
    w_epsilon = f_p*f_q
    b_epsilon = tf.squeeze(f_q)
     # w = w_mu + w_sigma*w_epsilon
    self.w = self.w_mu + tf.multiply(self.w_sigma, w_epsilon)
    ret = tf.matmul(inputs, self.w)

    # b = b_mu + b_sigma*b_epsilon
    self.b = self.b_mu + tf.multiply(self.b_sigma, b_epsilon)
    if self.activation_fn is None:
      return ret + self.b
    else:
      return self.activation_fn(ret + self.b)

  def get_config(self):
    config = super(noisy_dense, self).get_config()
    config.update({
        'units':
            self.units,
        'activation':
            activations.serialize(self.activation)
    })
    return config

  def compute_output_shape(self, input_shape):
    input_shape = tensor_shape.TensorShape(input_shape)
    input_shape = input_shape.with_rank_at_least(2)
    if tensor_shape.dimension_value(input_shape[-1]) is None:
      raise ValueError(
          'The innermost dimension of input_shape must be defined, but saw: %s'
          % input_shape)
    return input_shape[:-1].concatenate(self.units)