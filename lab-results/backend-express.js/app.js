// Import required packages
const express = require('express');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory database for demo purposes
let items = [
  { id: 1, name: 'Apples', quantity: 5 },
  { id: 2, name: 'Bread', quantity: 2 },
  { id: 3, name: 'Milk', quantity: 1 }
];

// Helper function to find next ID
const getNextId = () => {
  const maxId = items.reduce((max, item) => (item.id > max ? item.id : max), 0);
  return maxId + 1;
};

// GET all items
app.get('/items', (req, res) => {
  res.status(200).json(items);
});

// GET item by ID
app.get('/items/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = items.find(item => item.id === itemId);
  
  if (!item) {
    return res.status(404).json({ message: 'Item not found' });
  }
  
  res.status(200).json(item);
});

// POST create new item or update existing one if name already exists
app.post('/items', (req, res) => {
  const { name, quantity } = req.body;
  
  // Basic validation
  if (!name || typeof quantity !== 'number') {
    return res.status(400).json({ message: 'Name is required and quantity must be a number' });
  }
  
  // Check if an item with this name already exists
  const existingItemIndex = items.findIndex(item => item.name.toLowerCase() === name.toLowerCase());
  
  if (existingItemIndex !== -1) {
    // Update existing item quantity
    items[existingItemIndex].quantity += quantity;
    return res.status(200).json(items[existingItemIndex]);
  }
  
  // Create new item if name doesn't exist
  const newItem = {
    id: getNextId(),
    name,
    quantity
  };
  
  items.push(newItem);
  res.status(201).json(newItem);
});

// PUT update an item
app.put('/items/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const { name, quantity } = req.body;
  
  // Basic validation
  if (!name || typeof quantity !== 'number') {
    return res.status(400).json({ message: 'Name is required and quantity must be a number' });
  }
  
  const itemIndex = items.findIndex(item => item.id === itemId);
  
  if (itemIndex === -1) {
    return res.status(404).json({ message: 'Item not found' });
  }

  // Check if an item with the new name exists (but is not the current item)
  const existingItemWithSameName = items.find(item => 
    item.name.toLowerCase() === name.toLowerCase() && item.id !== itemId
  );
  
  if (existingItemWithSameName) {
    // If changing to an existing name, combine quantities and delete this item
    existingItemWithSameName.quantity += quantity;
    items.splice(itemIndex, 1);
    return res.status(200).json(existingItemWithSameName);
  }
  
  // Regular update if no name conflict
  items[itemIndex] = {
    id: itemId,
    name,
    quantity
  };
  
  res.status(200).json(items[itemIndex]);
});

// DELETE an item
app.delete('/items/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const itemIndex = items.findIndex(item => item.id === itemId);
  
  if (itemIndex === -1) {
    return res.status(404).json({ message: 'Item not found' });
  }
  
  // Remove the item
  items.splice(itemIndex, 1);
  
  res.status(204).send();
});

// Start the server
app.listen(PORT, () => {
  console.log(`Shopping API server running on port ${PORT}`);
});