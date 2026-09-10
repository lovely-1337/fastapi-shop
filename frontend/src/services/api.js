import axios from 'axios'

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const productsAPI = {
  getAll() {
    return apiClient.get('/products')
  },

  getById(id) {
    return apiClient.get(`/products/${id}`)
  },

  getByCategory(categoryId) {
    return apiClient.get(`/products/category/${categoryId}`)
  },
}

export const categoriesAPI = {
  getAll() {
    return apiClient.get('/categories')
  },

  getById(id) {
    return apiClient.get(`/categories/${id}`)
  },
}

export const cartAPI = {
  addItem(item, cartData) {
    return apiClient.post('/cart/add', {
      product_id: item.product_id,
      quantity: item.quantity,
      cart_data: cartData,
    })
  },

  getCart(cartData) {
    return apiClient.post('/cart', cartData)
  },

  updateItem(item, cartData) {
    return apiClient.put('/cart/update', {
      product_id: item.product_id,
      quantity: item.quantity,
      cart_data: cartData,
    })
  },

  removeItem(productId, cartData) {
    return apiClient.delete(`/cart/remove/${productId}`, {
      data: {
        cart_data: cartData,
      },
    })
  },
}

export default apiClient