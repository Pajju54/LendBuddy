var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

module.exports = app;

const multer = require('multer');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
// const path = require('path');  // Remove duplicate path import
const fs = require('fs');

// Configure file upload storage
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const uploadPath = path.join(__dirname, 'uploads/documents');
        fs.mkdirSync(uploadPath, { recursive: true });
        cb(null, uploadPath);
    },
    filename: (req, file, cb) => {
        const uniqueName = `${uuidv4()}${path.extname(file.originalname)}`;
        cb(null, uniqueName);
    }
});

// File validation
const fileFilter = (req, file, cb) => {
    if (file.mimetype === 'application/pdf') {
        cb(null, true);
    } else {
        cb(new Error('Only PDF files are allowed'), false);
    }
};

const upload = multer({
    storage: storage,
    fileFilter: fileFilter,
    limits: { fileSize: 5 * 1024 * 1024 } // 5MB limit
});

// Enable body parsing
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Document upload endpoint
app.post('/api/upload-documents', upload.fields([
    { name: 'pan', maxCount: 1 },
    { name: 'aadhar', maxCount: 1 }
]), (req, res) => {
    try {
        if (!req.files['pan'] || !req.files['aadhar']) {
            return res.status(400).json({ error: 'Both PAN and Aadhar files required' });
        }

        // Process uploaded files
        const documents = {
            pan: req.files['pan'][0].path,
            aadhar: req.files['aadhar'][0].path
        };

        res.status(200).json({
            message: 'Documents uploaded successfully',
            documents: documents
        });

    } catch (error) {
        res.status(500).json({
            error: 'Document upload failed',
            details: error.message
        });
    }
});
