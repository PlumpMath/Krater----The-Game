using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace WindowsGame1 {

    public class Game1 : Microsoft.Xna.Framework.Game {

        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        VertexBuffer vertexbuffer;
        VertexPositionColor[] verts;
        BasicEffect effect;
        Matrix world = Matrix.Identity;

        camera camera;

        public Game1() {
            camera = new camera(this, 
                                new Vector3(0, 0, 5),
                                Vector3.Zero, 
                                Vector3.Up);
            Components.Add(camera);

            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        protected override void Initialize() {

            // Set cullmode to none
            RasterizerState rs = new RasterizerState();
            rs.CullMode = CullMode.None;
            GraphicsDevice.RasterizerState = rs;

            base.Initialize();
        }

        protected override void LoadContent() {

            // Initialize vertices
            verts = new VertexPositionColor[3];
            verts[0] = new VertexPositionColor(new Vector3(0, 1, 0), Color.Blue);
            verts[1] = new VertexPositionColor(new Vector3(1, -1, 0), Color.Red);
            verts[2] = new VertexPositionColor(new Vector3(-1, -1, 0), Color.Green);

            vertexbuffer = new VertexBuffer(GraphicsDevice, typeof(VertexPositionColor),
            verts.Length, BufferUsage.None);
            vertexbuffer.SetData(verts);

            effect = new BasicEffect(GraphicsDevice);

            spriteBatch = new SpriteBatch(GraphicsDevice);
        }

        protected override void UnloadContent() {
            // Descargar Contenido
        }

        protected override void Update(GameTime gameTime) {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed) this.Exit();

            // Translation
            KeyboardState keyboardState = Keyboard.GetState();
            if (keyboardState.IsKeyDown(Keys.Left))
                world *= Matrix.CreateTranslation(-.01f, 0, 0);
            if (keyboardState.IsKeyDown(Keys.Right))
                world *= Matrix.CreateTranslation(.01f, 0, 0);

            world *= Matrix.CreateRotationY(MathHelper.PiOver4 / 60);

            base.Update(gameTime);
        }

        protected override void Draw(GameTime gameTime) {
            GraphicsDevice.Clear(Color.Black);
            GraphicsDevice.SetVertexBuffer(vertexbuffer);

            //Set object and camera info
            effect.World = world;
            //effect.World = Matrix.Identity;
            effect.View = camera.view;
            effect.Projection = camera.projection;
            effect.VertexColorEnabled = true;
            // Begin effect and draw for each pass
            foreach (EffectPass pass in effect.CurrentTechnique.Passes)
            {
                pass.Apply();
                GraphicsDevice.DrawUserPrimitives<VertexPositionColor>
                (PrimitiveType.TriangleStrip, verts, 0, 1);
            }

            base.Draw(gameTime);
        }
    }
}
